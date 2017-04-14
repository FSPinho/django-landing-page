import { fork } from 'redux-saga/effects'

import model from 'api/sagas/model'

export default function* () {
    yield fork(model)
}