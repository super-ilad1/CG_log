//获取path库，这个path库是默认的，所以可以直接使用
let path = require("path");
module.exports = {
    resolve: {
        modules: [path.resolve(__dirname, 'node_modules')]
    },
    mode: "production",//开发模式
    entry: "D:\\PycharmProject\\CG_log_web\\static", //打包文件的位置
    output: {
        filename: "bundle.js", //文件打包完成后的文件名
        path: 'D:\\PycharmProject\\CG_log_web\\static\\bundle' //文件打包后放在哪个目录下
    },
    plugins: [],

    module: {
        rules: [
            {
                test: /\.css$/,
                use: [ 'css-loader']
            }
        ]
    }


};