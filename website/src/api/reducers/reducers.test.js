import model from 'api/reducers/model'
import { actions } from 'api/actions'

it('Verify if model reducer works', () => {
    expect(
        model(undefined, {
            type: actions.model.done.load,
            payload: {
                page: [{ name: 'Home' }],
                pageLink: [{ page: 'home-page' }],
                socialLink: [[{ name: 'facebook' }]],
            }
        }).toJS()
    ).toEqual({
        status: {
            isLoading: false,
        },
        model: {
            page: [{ name: 'Home' }],
            pageLink: [{ page: 'home-page' }],
            socialLink: [[{ name: 'facebook' }]],
        }
    })
})