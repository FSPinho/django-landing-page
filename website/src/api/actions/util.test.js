import {join, createAction, createDispatcher} from 'api/actions/util';

it('Verify if join is working', () => {

    expect(join('a', 'b')).toBe('a - b');

});

it('Verify if createAction is working', () => {

    expect(
        createAction({
            anyThing: 'ANYTHING'
        })
    ).toEqual({
        do: {
            anyThing: '@@homeless-app - DO - ANYTHING'
        },
        doing: {
            anyThing: '@@homeless-app - DOING - ANYTHING'
        },
        done: {
            anyThing: '@@homeless-app - DONE - ANYTHING'
        },
        fail: {
            anyThing: '@@homeless-app - FAIL - ANYTHING'
        }
    });

});
