module.exports = function(grunt) {

    grunt.initConfig({
        ts: {
            default : {
                src: ["**/*.ts",
                      "!node_modules/**/*.ts",
                      "!**/*.d.ts"],
                outDir: "goz/static/js/built"
            },
            options: {
                compiler: './node_modules/typescript/bin/tsc',
                target: "es5",
                module: "amd"
            }
        }
    });

    // Default task(s).
    grunt.loadNpmTasks("grunt-ts");
    grunt.registerTask("default", ["ts"]);
};
