import { cookies } from "next/headers";
import { NextResponse } from "next/server";
import { ConnectDb } from "../../../lib/db/dbConnection";
import { verifyToken } from "../../../lib/jwt/token";
import UserModel from "../../../lib/db/schema/userSchema";



export async function GET() {
  await ConnectDb();

  const token = (await cookies()).get("session")?.value;
  if (!token) {
    return NextResponse.json(
      { msg: "Unauthorize request", success: false },
      { status: 401 }
    );
  }

  const verify = await verifyToken(token as string);
  if (!verify) {
    return NextResponse.json(
      { msg: "Invalid Token OR may be expired", success: false },
      { status: 401 }
    );
  }

  const findUser = await UserModel.findById({ _id: verify?.id }).select(
    "_id email userName"
  );
  return NextResponse.json({ ...findUser, sucess: true }, { status: 200 });
}
