import React from "react";

const Error404 = ({location} ) => {
    return(
         <div className="container">
                <div className="footer_bottom">
                    <h2 className="foot_right"> Error 404 page:'{location.pathname}' not found.</h2>
                </div>
        </div>
    )
}

export default Error404;
