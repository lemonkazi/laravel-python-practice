"use server";

import { cookies } from "next/headers";

export async function LogoutAction() {
  (await cookies()).delete("session");
}
