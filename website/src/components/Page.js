import React, { Component } from 'react'
import { connect } from 'react-redux'
import MobileDetect from 'mobile-detect'
import { Toolbar, ToolbarGroup, ToolbarTitle, FlatButton } from 'material-ui'

class Page extends Component {

    render() {
        const pages = this.props.store.model.getIn(['model', 'page']).toJS()
        const page = pages.filter(p => (p.name === this.props.page.name))[0]
        const pageLinks = this.props.store.model.getIn(['model', 'page-link']).toJS()

        const mobileDetect = new MobileDetect(window.navigator.userAgent)
        const isMobile = !!mobileDetect.mobile()

        return (
            <Toolbar>
                <ToolbarGroup firstChild={true}>
                    <ToolbarTitle style={{ marginLeft: 20 }} text={page.name} />
                </ToolbarGroup>
                <ToolbarGroup>
                    {
                        pageLinks.map(pl => (
                            <FlatButton key={pl.page.name} label={pl.page.name}/>
                        ))
                    }
                    {
                        pageLinks.map(pl => (
                            <FlatButton key={pl.page.name} label={pl.page.name}/>
                        ))
                    }
                </ToolbarGroup>
            </Toolbar>
        )
    }

}

export default connect((store) => ({ store }))(Page)