const { merge } = require("webpack-merge");
const TerserJSPlugin = require("terser-webpack-plugin");
const CssMinimizerPlugin = require("css-minimizer-webpack-plugin");

const common = require("./webpack.base.js");

module.exports = merge(common, {
  mode: "production",
  devtool: false,
  optimization: {
    minimizer: [
      new TerserJSPlugin(),
      new CssMinimizerPlugin()],
  },
});
