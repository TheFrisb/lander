/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./**/templates/**/*.html",
    "./**/templates/**/**/*.html",

    "./src/*.js",
    "./src/**/*.js",
  ],
  theme: {
    extend: {
      colors: {
        primary: "#0066FF",
        secondary: "#FFB800",
        accent: "#000000",
        background: "#F8FAFC",
        "text-dark": "#0F172A",
      },
      keyframes: {
        marquee: {
          "0%": { transform: "translateX(100%)" },
          "100%": { transform: "translateX(-100%)" },
        },
      },
      animation: {
        marquee: "marquee 20s linear infinite",
      },
    },
  },
  plugins: [],
};
