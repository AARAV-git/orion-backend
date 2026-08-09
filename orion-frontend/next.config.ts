import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  output: "standalone",
  typescript: {
    ignoreBuildErrors: true,
  },
  reactStrictMode: false,
  env: {
    PORT: process.env.PORT || "3000",
  },
};

export default nextConfig;
