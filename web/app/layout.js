export const metadata = { title: "APIM timeout lab" };

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body
        style={{
          fontFamily: "system-ui, sans-serif",
          margin: 0,
          background: "#f6f7f9",
          color: "#1b1f24",
        }}
      >
        {children}
      </body>
    </html>
  );
}
