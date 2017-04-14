import {join, createAction, createDispatcher} from 'api/actions/util';

const MODEL = 'MODEL';
const model = {
    load: join(MODEL, 'LOAD'),
};

export const actions = {
    model: createAction(model),
}

export const dispatchers = createDispatcher({
    'modelDispatcher': model,
});