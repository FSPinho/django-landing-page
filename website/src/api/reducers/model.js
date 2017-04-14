import { fromJS } from 'immutable'

const defaultDataEntry = {
    link: '',
    data: null
}

const initialState = fromJS({
    status: {
        isLoading: false, 
    }, 
    root: {
        ...defaultDataEntry, 
        data: {
            page: {}, 
            toolbar: {},
            pageLink: {},
            socialLink: {},
            toolbar: {}
        }
    }
})