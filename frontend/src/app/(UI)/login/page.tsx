"use client";
import Link from "next/link";
import React, {
  useActionState,
  useEffect,
} from "react";
import { useRouter } from "next/navigation";
import toast from "react-hot-toast";
import Image from "next/image";
import { LoginAction } from "../../(Actions)/loginAction";
import { FormInput } from "../../../components/FormInput";

export default function Login() {
  const [state, formAction, isLoading] = useActionState(LoginAction, {
    success: false,
    email: "",
  });
  const router = useRouter();

  // react to state update
  useEffect(() => {
    if (state?.logIn) {
      toast.success(`${state.logIn}`);
      setTimeout(() => {
        router.push("/");
      }, 400);
    }

    if (state?.logInErr) {
      toast.error(`${state.logInErr}`);
    }
  }, [state, router]);

 
  return (
    <section className="flex h-screen items-center justify-center bg-gray-900">
      <form
        action={formAction}
        className="bg-gray-800 p-8 rounded-2xl shadow-md w-full max-w-sm"
      >
        <h2 className="text-2xl text-white mb-6 text-center">Login</h2>
        <FormInput
          labelFor="email"
          label="Email"
          name="email"
          type="email"
          placeholder="you@example.com"
        />
        <h3 className="text-[#ff3d45] text-sm mb-1 ">{state?.email}</h3>
        <FormInput
          labelFor="password"
          label="Password"
          name="password"
          type="password"
          placeholder="••••••••"
        />
        <h3 className="text-[#ff3d45] text-sm mb-1 ">{state?.password}</h3>
        <button
          type="submit"
          disabled={isLoading}
          className={`w-full bg-green-600 text-white py-2 rounded-lg hover:bg-green-700 transition mt-3 mb-5 flex justify-center ${
            isLoading && "disabled:bg-green-700"
          } cursor-pointer`}
        >
          {isLoading ? (
            <Image
              src={"/loading.gif"}
              width={25}
              height={25}
              alt="loading_gif"
            />
          ) : (
            "Login"
          )}
          
        </button>

        <h2 className="text-xs text-slate-400">
          {"Do You Haven't Any Account"}
          <Link href={"/signup"} className=" ml-1 underline">
            Signup Now
          </Link>
        </h2>
      </form>
    </section>
  );
}
