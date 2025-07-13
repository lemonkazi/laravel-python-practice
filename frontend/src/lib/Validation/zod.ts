import * as z from "zod/v4";

export const User = z.object({
  userName: z
    .string()
    .trim()
    .min(4, "Username must be at least 4 characters")
    .max(9, "Must not exceed 9 characters")
    .regex(/\d/, "Username must contain at least one number"),
  email: z.email("Enter a valid email address").lowercase().trim(),
  password: z
    .string()
    .trim()
    .min(6, "Password must be at least 6 characters")
    .max(14, "Must not exceed 14 characters")
    .regex(
      /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$/,
      "Password must include uppercase, lowercase, number, and special character"
    ),
});

export const loginSchema = z.object({
  email: z.email("Enter a valid email address").trim(),
  password: z.string().min(6, "Password must be at least 6 characters"),
});
