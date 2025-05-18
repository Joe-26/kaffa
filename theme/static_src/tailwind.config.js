/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    /**
     * HTML. Paths to Django template files that will contain Tailwind CSS classes.
     */

    // Capture HTML files in any 'templates' directory within any app in your project.
    '../../../**/templates/**/*.html',
    '../../../**/templates/*.html',
    '../../../base/templates/base.html',

  ],
  theme: {
    extend: {
      fontFamily: {
        googleMono: ['Atkinson Hyperlegible Mono', 'sans-serif'],
        handWrite: ['Mynerve', 'cursive'],
        boldHead: ['Ranchers', 'sans-serif'],
        sansBody: ['Ancizar Sans', 'sans-serif']
      }
    },
  },
  plugins: [],
}