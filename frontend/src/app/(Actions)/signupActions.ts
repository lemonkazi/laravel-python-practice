"use server";
import * as z from "zod/v4";
import { ConnectDb } from "../../lib/db/dbConnection";
import { User } from "../../lib/Validation/zod";
import UserModel from "../../lib/db/schema/userSchema";

export type SignupState = {
  success: boolean;
  userName?: string[];
  email?: string[] | string;
  password?: string[];
  signupErr?: string;
  signup?: string;
};

export async function SignupAction(
  _state: SignupState,
  formData: FormData
): Promise<SignupState> {
  try {
    await ConnectDb();

    const userData = Object.fromEntries(formData);
    const { error, data } = User.safeParse(userData);

    if (error) {
      const flattened = z.flattenError(error).fieldErrors;

      return {
        success: false,
        userName: flattened.userName,
        email: flattened.email,
        password: flattened.password,
      };
    }

    const existingUser = await UserModel.findOne({ email: data?.email });
    if (existingUser) {
      return {
        success: false,
        email: "This email is already registered",
      };
    }

    const newUser = new UserModel(data);
    await newUser.save();

    return {
      success: true,
      signup: "Successfully signed up",
    };
  } catch (error) {
    console.error(error);
    return {
      success: false,
      signupErr: "Something went wrong",
    };
  }
}
