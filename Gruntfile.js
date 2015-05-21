module.exports = function(grunt) {

    grunt.loadNpmTasks("grunt-tsc");

    grunt.initConfig({
        tsc: {
            options: {
                // global options
                target: "es5",
                module: "amd",
                version: "1.5"
            },
            task_name: {
                options: {},
                files: [{
                    expand : true,
                    dest   : "goz/static/js/built",
                    cwd    : "goz/static/ts",
                    ext    : ".js",
                    src    : [
                        "**/*.ts",
                        "!**/*.d.ts"
                    ]
                }]
            }
        }
    });

    // Default task(s).
    grunt.registerTask('default', ['tsc']);

};
