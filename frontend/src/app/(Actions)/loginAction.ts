"use server";

import bcrypt from "bcryptjs";
import { cookies } from "next/headers";
import * as z from "zod/v4";
import { ConnectDb } from "../../lib/db/dbConnection";
import { loginSchema } from "../../lib/Validation/zod";
import UserModel from "../../lib/db/schema/userSchema";
import { genToken } from "../../lib/jwt/token";

type stateTyp = {
  email?: string | string[];
  password?: string | string[];
  success: boolean;
  logIn?: string;
  loginErr?: string;
};

export async function LoginAction(state: stateTyp, formData: FormData) {
  try {
    await ConnectDb();

    const user = Object.fromEntries(formData);

    // --> validation phase
    const { data, error } = loginSchema.safeParse(user);

    if (error) {
      const flattened = error ? z.flattenError(error).fieldErrors : {};
      return { ...flattened, success: false };
    }

    // ---> db operation
    const findUser = await UserModel.findOne({ email: data?.email });
    if (!findUser) {
      return { email: "Email does not exist", success: false };
    }

    const comparePassword = await bcrypt.compare(
      data?.password as string,
      findUser.password
    );
    if (!comparePassword) {
      return { password: "Incorrect password", success: false };
    }

    const jwtToken = genToken(findUser?._id as string);
    const expiresAt = new Date(Date.now() + 50 * 60 * 1000);
    (await cookies()).set("session", jwtToken, {
      httpOnly: true,
      sameSite: "strict",
      secure: true,
      expires: expiresAt,
    });

    return { logIn: "SucessFully logged In", success: true };
  } catch (error) {
    console.log(error);
    return { logInErr: "Something went to wrong", success: false };
  }
}
