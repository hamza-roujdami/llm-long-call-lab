import { NextResponse } from "next/server";

// Lab guard: the UI can start paid model runs, so it sits behind HTTP basic auth (LAB_PASSWORD).
export function middleware(req) {
  const password = process.env.LAB_PASSWORD;
  if (!password) return NextResponse.next();
  const header = req.headers.get("authorization") || "";
  if (header.startsWith("Basic ")) {
    const [, pass] = atob(header.slice(6)).split(/:(.*)/s);
    if (pass === password) return NextResponse.next();
  }
  return new NextResponse("Authentication required", {
    status: 401,
    headers: { "WWW-Authenticate": 'Basic realm="apim-timeout-lab"' },
  });
}

export const config = { matcher: "/((?!_next/static|_next/image|favicon.ico).*)" };
