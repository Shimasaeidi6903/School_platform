import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "سامانه جامع مدرسه",
  description: "سامانه جامع مدیریت مدرسه",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="fa" dir="rtl">
      <body>{children}</body>
    </html>
  );
}
