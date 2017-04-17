import React, { Component } from 'react'
import { Animated, Easing } from 'react-native';

class FadeDownUp extends Component {

    constructor(props) {
        super(props)

        this.state = {
            fadeAnim: new Animated.Value(0),
            translationAnim: new Animated.Value(50),
        }
    }

    componentDidMount() {
        Animated.parallel([
            Animated.timing(
                this.state.fadeAnim,
                {
                    toValue: 1,
                    easing: Easing.inOut(Easing.cubic)
                }
            ),
            Animated.timing(
                this.state.translationAnim,
                {
                    toValue: 0,
                    easing: Easing.inOut(Easing.cubic)
                }
            )
        ]).start()
    }

    render() {

        return (
            <Animated.View
                style={{
                    opacity: this.state.fadeAnim,
                    marginTop: this.state.translationAnim
                }}
            >
                {this.props.children}
            </Animated.View>
        )
    }

}

export default FadeDownUp