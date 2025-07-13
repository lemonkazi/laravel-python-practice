"use client";
import Link from "next/link";
import React, { useEffect } from "react";
import toast from "react-hot-toast";
import { useRouter } from "next/navigation";
import { useActionState } from "react";
import { SignupAction, SignupState } from "../../(Actions)/signupActions";
import { FormInput } from "../../../components/FormInput";



const initialState: SignupState = {
  success: false,
  userName: [],
  email: [],
  password: [],
  signupErr: undefined,
  signup: undefined,
};

export default function Signup() {
  const [state, formAction] = useActionState(SignupAction, initialState);
  const router = useRouter();

  useEffect(() => {
    if (state.signup) {
      toast.success(`${state.signup}`);
      setTimeout(() => {
        router.push("/login");
      }, 400);
    }

    if (state.signupErr) {
      toast.error(`${state.signupErr}`);
    }
  }, [state, router]);

  return (
    <section className="flex h-screen items-center justify-center bg-gray-900">
      <form
        action={formAction}
        className="bg-gray-800 p-8 rounded-2xl shadow-md w-full max-w-sm"
      >
        <h2 className="text-2xl text-white mb-6 text-center">Sign Up</h2>

        {/* Username Field */}
        <FormInput
          labelFor="username"
          label="User Name"
          name="userName"
          placeholder="Your name"
        />
        {state.userName?.map((err, index) => (
          <h3 key={index} className="text-[#ff3d45] text-sm mb-1">
            ❌ {err}
          </h3>
        ))}

        {/* Email Field */}
        <FormInput
          labelFor="email"
          label="Email"
          name="email"
          type="email"
          placeholder="you@example.com"
        />
        {typeof state.email === "string" ? (
          <h3 className="text-[#ff3d45] text-sm mb-1">❌ {state.email}</h3>
        ) : (
          state.email?.map((err, index) => (
            <h3 key={index} className="text-[#ff3d45] text-sm mb-1">
              ❌ {err}
            </h3>
          ))
        )}

        {/* Password Field */}
        <FormInput
          labelFor="password"
          label="Password"
          name="password"
          type="password"
          placeholder="••••••••"
        />
        {state.password?.map((err, index) => (
          <h3 key={index} className="text-[#ff3d45] text-sm mb-1">
            ❌ {err}
          </h3>
        ))}

        {/* Submit */}
        <button
          type="submit"
          className="w-full bg-green-600 text-white py-2 rounded-lg hover:bg-green-700 transition mt-3 mb-5"
        >
          Sign Up
        </button>

        <h2 className="text-xs text-slate-400 text-center">
          Already have an account?{" "}
          <Link href={"/login"} className="underline">
            Login Now
          </Link>
        </h2>
      </form>
    </section>
  );
}
