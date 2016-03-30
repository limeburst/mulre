var yarns = [];
var evtSource = new EventSource('/streams/firehose/');

evtSource.onmessage = function(e) {
    yarns.unshift(JSON.parse(e.data));
    ReactDOM.render(
        <YarnList yarns={yarns} />,
        document.getElementById('stream')
    );
};

var YarnList = React.createClass({
    render: function() {
        var yarnNodes = this.props.yarns.map(function(yarn) {
            return (
                <Yarn key={yarn.id} id={yarn.id} content={yarn.content} tags={yarn.tags} />
            )
        });
        return (
            <div className="yarn-list">
                {yarnNodes}
            </div>
        )
    }
});

var Yarn = React.createClass({
    render: function() {
        if (this.props.tags.length) {
            var tagNodes = this.props.tags.map(function (tag) {
                return (
                    <Tag key={tag} name={tag}/>
                )
            });
        } else {
            var tagNodes = "태그 없음";
        }
        return (
            <article className="yarn">
                <ul className="metadata">
                    <li className="yarn-id">
                        <a href={'/yarns/' + this.props.id + '/'}>
                            {this.props.id}
                        </a>
                    </li>
                    <li>
                        <ul className="tags">
                            {tagNodes}
                        </ul>
                    </li>
                </ul>
                <pre>{this.props.content}</pre>
            </article>
        )
    }
});

var Tag = React.createClass({
    render: function() {
        return (
            <li>
                <a href={'/tags/' + this.props.name + '/'}>{this.props.name}</a>
            </li>
        )
    }
});
