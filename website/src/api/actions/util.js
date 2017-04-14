const NAMESPACE = '@@homeless-app';
const DO = 'DO';
const DOING = 'DOING';
const DONE = 'DONE';
const FAIL = 'FAIL';
const SEPARATOR = ' - ';

/* UTILS */

const _join = (...args) => (
    args.reduce((a, b) => (a + SEPARATOR + b))
);

export const join = _join;

const _prefix = (...args) => (
    _join(NAMESPACE, ...args)
);

const _do = (...args) => (
    _prefix(DO, ...args)
);

const _doing = (...args) => (
    _prefix(DOING, ...args)
);

const _done = (...args) => (
    _prefix(DONE, ...args)
);

const _fail = (...args) => (
    _prefix(FAIL, ...args)
);

export const createAction = (action) => {
    const _action = {
        do: {},
        doing: {},
        done: {},
        fail: {}
    };
    for (let k in action) {
        if(k) {
            _action.do[k] = _do(action[k]);
            _action.doing[k] = _doing(action[k]);
            _action.done[k] = _done(action[k]);
            _action.fail[k] = _fail(action[k]);
        }
    }
    return _action;
};

export const createDispatcher = (actions) => {
    return (dispatch) => {
        const _dispatcher = {};
        for (let actionName in actions) {
            if(actionName) {
                let action = actions[actionName];
                _dispatcher[actionName] = {
                    do: {},
                    doing: {},
                    done: {},
                    fail: {}
                };
                for (let k in action) {
                    if(k) {
                        _dispatcher[actionName].do[k] = payload => dispatch({type: _do(action[k]), payload});
                        _dispatcher[actionName].doing[k] = payload => dispatch({type: _doing(action[k]), payload});
                        _dispatcher[actionName].done[k] = payload => dispatch({type: _done(action[k]), payload});
                        _dispatcher[actionName].fail[k] = payload => dispatch({type: _fail(action[k]), payload});
                    }
                }
            }
        }

        return _dispatcher;
    };
};
