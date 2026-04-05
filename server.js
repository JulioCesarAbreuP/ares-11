import express from "express";
import telemetryRoute from "./core/telemetry/telemetryRoute.js";

const app = express();
const PORT = process.env.PORT || 3000;

app.use("/api", telemetryRoute);

app.listen(PORT, () => {
  console.log(`ARES-11 API listening on port ${PORT}`);
});
