const path = require("path");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
  entry: {
    site: path.resolve(__dirname, "../frontend/index.js"),
  },
  output: {
    path: path.resolve(
      __dirname,
      "../{{cookiecutter.project_slug}}/static/dist"
    ),
    publicPath: "",
    filename: "[name].js",
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: ["babel-loader"],
      },
      {
        test: /\.(s?)css$/,
        use: [MiniCssExtractPlugin.loader, "css-loader", "sass-loader"],
      },
      {
        test: /\.(eot|ttf|woff|woff2|svg)$/,
        use: {
          loader: "file-loader",
          options: {
            name: "assets/[name].[ext]",
          },
        },
      },
    ],
  },
  optimization: {
    splitChunks: {
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: "vendor",
          chunks: "all",
        },
      },
    },
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: "[name].css",
    }),
  ],
};
