import jwt from "jsonwebtoken";
export type DecodedToken = {
  id: string;
  iat?: number;
  exp?: number;
};
const tokenSec = process.env.TOKEN_SEC;

export function genToken(id: string) {
  const token = jwt.sign({ id }, `${tokenSec}`, {
    expiresIn: "50m",
  });
  return token;
}

export async function verifyToken(token: string): Promise<DecodedToken | null> {
  try {
    const decoded = jwt.verify(token, `${tokenSec}`) as unknown as DecodedToken;
    return decoded;
  } catch {
    return null;
  }
}
