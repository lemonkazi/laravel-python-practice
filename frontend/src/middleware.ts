import { cookies } from "next/headers";
import { NextRequest, NextResponse } from "next/server";

export async function middleware(req: NextRequest) {
  const token = (await cookies()).get("session")?.value;

  const currentPath = req.nextUrl.pathname;
  const isPublicPath = currentPath === "/login" || currentPath === "/signup";
  
  if (token && isPublicPath) {
    return NextResponse.redirect(new URL("/", req.url));
  }

  if (!token && !isPublicPath) {
    return NextResponse.redirect(new URL("/login", req.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: ["/", "/login", "/signup"],
};
