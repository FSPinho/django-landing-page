import React, { Component } from 'react'
import { connect } from 'react-redux'
import MobileDetect from 'mobile-detect'
import muiThemeable from 'material-ui/styles/muiThemeable'
import { Drawer, MenuItem } from 'material-ui'

import { FadeDownUp } from 'components/animations'

class Section extends Component {

    render() {
        const mobileDetect = new MobileDetect(window.navigator.userAgent)
        const isMobile = !!mobileDetect.mobile()

        const theme = this.props.muiTheme
        const section = this.props.section
        const backgroundImage = isMobile ? section.backgroundImageLarge : section.backgroundImageMedium
        const backgroundColor = section.backgroundColor ? section.backgroundColor.value : null
        return (
            <FadeDownUp>
                <div
                    style={{
                        height: (section.fullHeight ? `calc(100vh - 2 * ${theme.appBar.height}px)` : 'auto'),
                        background: `${backgroundColor} url('${backgroundImage}') center / cover`,
                        paddingTop: theme.appBar.height,
                        paddingBottom: theme.appBar.height,
                    }}
                >
                    Section {section.id}
                </div>
            </FadeDownUp>
        )
    }

}

const SectionThemeable = muiThemeable()(Section)
export default connect((store) => ({ store }))(SectionThemeable)