// Server-side proxy to the internal api, so the browser never needs the api address.
const API = (process.env.API_URL || "http://localhost:8080").replace(/\/$/, "");

async function proxy(req, { params }) {
  const { path } = await params;
  const url = `${API}/${path.join("/")}${new URL(req.url).search}`;
  const init = { method: req.method, headers: { "content-type": "application/json" }, cache: "no-store" };
  if (req.method !== "GET" && req.method !== "HEAD") init.body = await req.text();
  const r = await fetch(url, init);
  const headers = { "content-type": r.headers.get("content-type") || "application/json" };
  const disposition = r.headers.get("content-disposition");
  if (disposition) headers["content-disposition"] = disposition;
  return new Response(r.body, { status: r.status, headers });
}

export const dynamic = "force-dynamic";
export { proxy as GET, proxy as POST };
