import config from 'api/service/config'

const _getApiRoot = (format) => {
    return fetch(`${config.apiRootURL}?format=${format}`).then(data => data.json())
}

const _getModel = (model, url) => {
    return new Promise((acept, reject) => {
        fetch(url)
            .then(data => data.json())
            .then(json => {
                acept({ [model]: json })
            })
            .catch(reject)
    })
}

export const getModels = (format = 'json') => {
    return new Promise((a, r) => {

        _getApiRoot(format).then(apiRoot => {

            const promises = Object.keys(apiRoot).map(k => (
                _getModel(k, apiRoot[k])
            ))

            Promise.all([
                ...promises
            ]).then(models => [
                a(models.reduce((a, b) => ({ ...a, ...b })))
            ]).catch(r)

        })


    })
}

export default {
    getModels
}