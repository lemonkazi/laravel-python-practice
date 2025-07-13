"use client";
import axios from "axios";
import Image from "next/image";
import { useEffect, useState } from "react";
import { FiLogOut } from "react-icons/fi";
import { LogoutAction } from "./(Actions)/logoutAction";
import { useRouter } from "next/navigation";

export default function Home() {
  const router = useRouter();
  const [user, setData] = useState({ userName: "", email: "", _id: "" });
  useEffect(() => {
    axios
      .get("/user", { withCredentials: true })
      .then((result) => setData(result.data._doc));
  }, []);

  return (
    <section className="w-full h-screen flex justify-center items-center bg-gradient-to-br from-gray-800 via-gray-900 to-black">
      <div className="bg-white shadow-xl rounded-xl p-6 w-[350px] text-center relative">
        {/* Logout button */}
        <div className="absolute top-4 right-4">
          <button
            type="button"
            className="text-red-500 hover:text-red-600 transition cursor-pointer transform hover:scale-105"
            onClick={async () => {
              await LogoutAction();
              router.push("/login");
              router.refresh();
            }}
          >
            <FiLogOut size={25} />
          </button>
        </div>

        {/* Profile avatar */}
        <div className="flex flex-col items-center gap-4">
          <Image
            src={"/avatar.png"}
            alt="avatar"
            width={120}
            height={120}
            className="rounded-full border-4 border-white shadow-md"
          />

          {/* Username */}
          <h2 className="text-xl font-semibold text-gray-800">
            {user?.userName ?? "Anonymous"}
          </h2>

          {/* Email */}
          <h1 className="text-sm text-gray-500">
            {user?.email ?? "no-email@example.com"}
          </h1>
        </div>
      </div>
    </section>
  );
}
