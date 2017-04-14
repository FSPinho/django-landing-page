import { takeLatest, put } from 'redux-saga/effects'

import { actions } from 'api/actions'
import { crud } from 'api/service'

function* doLoadModel() {
    
    try {
        const payload = yield crud.getModels()
        yield put({ type: actions.model.done.load, payload })
    } catch(err) {
        yield put({ type: actions.model.fail.load, payload: err })
    }
    

}

export default function* () {
    yield takeLatest(actions.model.do.load, doLoadModel)
}