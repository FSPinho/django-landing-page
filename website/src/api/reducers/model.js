import { fromJS } from 'immutable'
import { actions } from 'api/actions'

const initialState = fromJS({
    status: {
        isLoading: false,
    },
    model: {
        page: [],
        pageLink: [],
        socialLink: [],
    }
})

export default (state = initialState, action) => {
    if (action.type === actions.model.done.load) {
        console.log(action.payload)
        state = state.set('model', action.payload)
        console.log(state.toJS())
    }

    return state
}