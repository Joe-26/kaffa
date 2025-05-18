/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    /**
     * HTML. Paths to Django template files that will contain Tailwind CSS classes.
     */

    // Capture HTML files in any 'templates' directory within any app in your project.
    '../../../**/templates/**/*.html',

  ],
  theme: {
    extend: {},
  },
  plugins: [],
}