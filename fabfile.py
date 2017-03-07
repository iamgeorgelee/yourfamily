from fabric.api import local

def webpack():
    local('rm -rf family_center/static/bundles/stage/*')
    local('rm -rf family_center/static/bundles/prod/*')
    local('webpack --config webpack.stage.config.js --progress --colors')
    local('webpack --config webpack.prod.config.js --progress --colors')
