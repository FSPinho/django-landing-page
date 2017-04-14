import config from 'api/service/config';

export const getApiRoot = (format='json') => {
    return fetch(`${config.apiRootURL}?format=${format}`)
        .then((response) => response.json())
}

export default {
    getApiRoot
}