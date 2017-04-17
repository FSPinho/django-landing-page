import React, { Component } from 'react'
import { connect } from 'react-redux'
import MobileDetect from 'mobile-detect'
import muiThemeable from 'material-ui/styles/muiThemeable'
import * as colors from 'material-ui/styles/colors'

import { FlatButton, GridList, GridTile, Toolbar, ToolbarTitle, ToolbarGroup } from 'material-ui'

class Footer extends Component {

    render() {
        const mobileDetect = new MobileDetect(window.navigator.userAgent)
        const isMobile = !!mobileDetect.mobile()

        const theme = this.props.muiTheme
        const footer = this.props.footer
        const pages = this.props.store.model.getIn(['model', 'page']).toJS()
            .sort((a, b) => (
                a.mainPage ? -1 : (b.mainPage ? 1 : (a.order - b.order))
            ))

        return (
            <GridList cols={12} cellHeight='auto'>
                <GridTile cols={12}
                    style={{
                        backgroundColor: colors.blueGrey700,
                    }}
                >
                    <Toolbar style={{ backgroundColor: colors.blueGrey700 }}>
                        <ToolbarGroup firstChild={true}>
                            <ToolbarTitle style={{
                                marginLeft: 20,
                                color: this.props.muiTheme.palette.alternateTextColor
                            }} text={footer.copyrightText} />
                        </ToolbarGroup>
                        <ToolbarGroup>
                            {
                                pages.filter(p => p.showInFooter).map(p => (
                                    <FlatButton key={p.name}
                                        style={{
                                            color: this.props.muiTheme.palette.alternateTextColor,
                                            marginLeft: 10,
                                            marginRight: 0,
                                        }}
                                        label={p.name}
                                        onTouchTap={() => this.onPageLinkClicked(p)} />)
                                )
                            }
                        </ToolbarGroup>
                    </Toolbar>
                </GridTile>
            </GridList>
        )
    }

}

const FooterThemeable = muiThemeable()(Footer)
export default connect((store) => ({ store }))(FooterThemeable)