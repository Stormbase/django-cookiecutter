const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const webpack = require('webpack');

const pkg = require('../package.json');


module.exports = {
  entry: {
    'app': path.resolve(__dirname, '../frontend/index.js'),
  },
  output: {
    path: path.resolve(__dirname, '../{{cookiecutter.project_slug}}/static/dist'),
    filename: '[name].js'
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: ["babel-loader"]
      },
      {
        test: /\.(s?)css$/,
        use: [MiniCssExtractPlugin.loader, "css-loader", "sass-loader"]
      },
      {
        test: /\.(eot|ttf|woff|woff2|svg)$/,
        use: {
          loader: "file-loader",
          options: {
            name: "assets/[name].[ext]"
          }
        }
      }
    ]
  },
  optimization: {
    splitChunks: {
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: "vendor",
          chunks: "all"
        }
      }
    },
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: '[name].css'
    }),
    new webpack.BannerPlugin({
      banner: `${pkg.name} ${pkg.version}
Copyright 2019-${new Date().getFullYear()}
`
    }),
  ],
  stats: "errors-only",
}