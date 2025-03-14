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

    },
  },
  plugins: [],
};
