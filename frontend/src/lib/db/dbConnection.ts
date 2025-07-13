import mongoose, { Connection } from "mongoose";

// ---> define  the shape of  cached connection
interface ConnectionCache {
  connection: Connection | null;
  promise: Promise<Connection> | null;
}

// ---> A custom global variable mongoose on the Node.js global object.
declare global {
  var mongoose: ConnectionCache;
}

// ---> Store global mongoose into a variable
let cached = global.mongoose;

// ---> If global.mongoose wasn't set yet, initialize it with null values.
if (!cached) {
  cached = global.mongoose = { connection: null, promise: null };
}

export async function ConnectDb() {
  try {
    // ---> If the database is already connected (conn is set), return it. This avoids creating a new connection every time the function runs.
    if (cached.connection) {
      console.log("Connection From Global Cache");
      return cached.connection;
    }

    // --->  If no connection is being made yet (promise is null), create one.
    if (!cached.promise) {
      // ---> bufferCommands: false disables command buffering, useful for avoiding unexpected behavior if the connection drops.
      const options = { bufferCommands: false };
      // ---> You initialize the cached.promise with the mongoose.connect().
      cached.promise = mongoose
        .connect(
          `mongodb+srv://${process.env.DB_USER}:${process.env.DB_KEY}@cluster0.nil1t1y.mongodb.net/${process.env.DB_NAME}`,
          options
        )
        .then((result) => {
          //---> Once the connection is successful, it returns the result.connection.
          console.log("🟢 Mongoose .connect() successful");
          return result.connection;
        });
    }

    // --->  Await the connection promise and cache the resolved connection.
    cached.connection = await cached.promise;

    //----> return the connection
    return cached.connection;
  } catch (error) {
    console.log("error From Db Connection", error);
  }
}
