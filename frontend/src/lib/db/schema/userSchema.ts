import mongoose, { Document, Model, Schema } from "mongoose";
import bcrypt from "bcryptjs";
interface IUser extends Document {
  userName: string;
  email: string;
  password: string;
  session?: string;
  sessionExp?: Date;
}

const UserSchema = new Schema<IUser>(
  {
    userName: {
      type: String,
      required: [true, "Please Provide User Name"],
      unique: true,
      trim: true,
    },
    email: {
      type: String,
      required: [true, "Please Provide User Email"],
      unique: true,
      trim: true,
    },
    password: {
      type: String,
      required: [true, "Please Enter Your Password"],
      trim: true,
    },

    session: String,
    sessionExp: Date,
  },
  { timestamps: true }
);

UserSchema.pre("save", async function (next) {
  const plain_password = this.password;
  if (!this.isModified("password")) {
    return next();
  }
  this.password = await bcrypt.hash(plain_password, 11);
  next();
});

const UserModel: Model<IUser> =
  mongoose.models.User || mongoose.model<IUser>("User", UserSchema);

export default UserModel;
