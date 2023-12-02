/***********************************************
                DOCUMENT ELEMENTS                   
***********************************************/
// - User Input
const functionInput = document.getElementById('function-input');
const lowerBoundInput = document.getElementById('lower-bound-input');
const upperBoundInput = document.getElementById('upper-bound-input');
const subIntervalInput = document.getElementById('sub-interval-input');
const calculateButton = document.getElementById('calculate-button');

// - UI Elements
const feedbackBox = document.getElementById('feedback-box');
const graphContainer = document.getElementById('graph-container');

/***********************************************
                    VARIABLES                   
***********************************************/
var feedbackMessage = '';

/***********************************************
                 FETCH REQUESTS             
***********************************************/
async function fetchPost( URL, formData ) {
    var response = await fetch( URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify( formData ),
    }); 
    return response;
}

/***********************************************
                 CALCULATE BUTTON           
***********************************************/
calculateButton.addEventListener( 'click', async function() {
    try {
        const areInputsEmpty = await areInputBoxesEmpty();
        if( areInputsEmpty ) {
            feedbackBox.style.display = 'block';
            feedbackBox.textContent = `${feedbackMessage}`;
            graphContainer.style.backgroundImage = `url('')`;
            return;
        }

        const calculateFormData = {
            functionValue: functionInput.value,
            lowerBoundValue: parseFloat(lowerBoundInput.value),
            upperBoundValue: parseFloat(upperBoundInput.value),
            subIntervalValue: parseFloat(subIntervalInput.value)
        }
        console.log( calculateFormData );

        const response = await fetchPost( '/calculate', calculateFormData )
        console.log( response.status );

        if( response.status !== 200 ) {
            feedbackBox.style.display = 'block';
            feedbackBox.textContent = 'Invalid Input: f(x)';
            
            return; // - Fetch failed
        }

        if( response.status === 500 ) {
            feedbackBox.style.display = 'block';
            feedbackBox.textContent = 'MatplotLib Error';
            return; // - Fetch failed
        }

        feedbackBox.style.display = 'none';
        const timestamp = new Date().getTime();
        graphContainer.style.backgroundImage = `url('static/plot.png?timestamp=${timestamp}')`;

    } catch( error ) {
        console.log( "Calculate Button Error: ", error );
    }
});

async function areInputBoxesEmpty() {
    const isFunctionEmpty = functionInput.value === '';
    const isLowerBoundEmpty = lowerBoundInput.value === '';
    const isUpperBoundEmpty = upperBoundInput.value === '';
    const isSubIntervalEmpty = subIntervalInput.value === '';

    if( isFunctionEmpty ) {
        feedbackMessage = 'f(x) is missing';
    } else if( isLowerBoundEmpty ) {
        feedbackMessage = 'a is missing';
    } else if( isUpperBoundEmpty ) {
        feedbackMessage = 'b is missing';
    } else if( isSubIntervalEmpty ) {
        feedbackMessage = 'n is missing';
    } 

    return isFunctionEmpty || isLowerBoundEmpty || 
           isUpperBoundEmpty || isSubIntervalEmpty;
}