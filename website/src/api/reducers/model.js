import { fromJS } from 'immutable'
import { actions } from 'api/actions'

const initialState = fromJS({
    status: {
        isLoading: true,
    },
    model: {
        'page': [],
        'page-link': [],
        'social-link': [],
    }
})

export default (state = initialState, action) => {

    if (action.type === actions.model.done.load) {
        return state.merge({ status: { isLoading: false }, model: action.payload })
    }

    return state
}