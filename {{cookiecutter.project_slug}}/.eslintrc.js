module.exports = {
  "extends": [
    // Use the Airbnb style guide as base
    // Read more: https://github.com/airbnb/javascript
    "airbnb-base",
  ],
  "parserOptions": {
    "parser": "babel-eslint"
  },
  "env": {
    "browser": true,
    "es6": true,
    "node": true
  },
  "rules": {
    "quotes": ["error", "double"],
    // Allow the use of console.log
    "no-console": "off",
    // Allow the use of i++
    "no-plusplus": "off",
  },
};
