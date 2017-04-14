import { takeLatest, put } from 'redux-saga/effects'

import { actions } from 'api/actions'
import { crud } from 'api/service'

function* doLoadModel() {
    
    try {
        const payload = yield crud.getApiRoot()
        put({ type: actions.model.fail.load, payload })
    } catch(err) {
        put({ type: actions.model.fail.load, payload: err })
    }
    

}

export default function* () {
    yield takeLatest(actions.model.do.load, doLoadModel)
}