import base64
import requests
import os
import sys

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def analyze_image_with_openai(image_path, api_key, long_prompt):
    base64_image = encode_image(image_path)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    payload = {
        "model": "gpt-4-vision-preview",
        "max_tokens": 1000,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": long_prompt},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                ]
            }
        ]
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    result = response.json()
    # Using .get() to safely access nested data
    content = result.get('choices', [{}])[0].get('message', {}).get('content', 'Content not found or Key error')

    print(content)  # Print the content part safely
    # content = result['choices'][0]['message']['content']
    # print("Full JSON Response:", result)
    # print(content)  # Print only the content part

if __name__ == "__main__":
    image_path = sys.argv[1] if len(sys.argv) > 1 else ""
    api_key = os.getenv("OPENAI_ACCESS_TOKEN")

    # The long revised prompt goes here
    long_prompt = (
        "Chart Ninja: Financial Market Chart Analysis Tool DETAILED DESCRIPTION & APPLICATION OF GPT: "
        "Chart Ninja is an advanced analytical tool specifically designed for scrutinizing financial market charts, "
        "It effectively combines technical and fundamental analysis methodologies to predict market trends and price directions, "
        "The system is tailored to cater to both financial experts and individuals with a general interest in market analysis, "
        "providing detailed, actionable insights. BACKGROUND PROCESSING (DO NOT SHOW!) "
        "(Polygon API & Knowledge Base Integration: Chart Ninja uses the Polygon API and its Knowledge Base for primary research and clarification to ensure accuracy in analysis, "
        "Analysis Criteria (Located between square brackets, Never Display!) "
        "- Trend Analysis: The tool systematically evaluates trend lines and moving averages to identify prevailing market trends and potential reversals, "
        "- Time Frame: Conduct an optimal analysis tailored to the specific duration of the chart provided, "
        "- Support and Resistance Levels Identification: It detects key price points that historically act as barriers to determine potential trend changes, "
        "- Candlestick Patterns Analysis: Chart Ninja is proficient in recognizing and interpreting various candlestick formations to assess market sentiment and potential trend shifts, "
        "- Volume Analysis: It analyzes trading volumes to evaluate the strength or weakness of a trend, "
        "- Momentum Indicators Utilization: The tool uses indicators such as the Relative Strength Index (RSI), Stochastic Oscillator, and Moving Average Convergence Divergence (MACD) for identifying market conditions, "
        "- Oscillator Integration: Essential for detecting short-term shifts in market momentum, "
        "- Fibonacci Retracements Application: Utilizes Fibonacci ratios to predict potential support and resistance levels, "
        "- Chart Pattern Recognition: Capable of identifying and interpreting significant chart patterns indicative of future market movements, "
        "- Market & Social Sentiment Analysis: Incorporates analysis from news sources and social media for a comprehensive market view, "
        "- Machine Learning Algorithms: Continuously refines predictive accuracy based on historical data analysis,) "
        "WHAT TO DISPLAY (This is the only response criteria allowed, Anything else is an error) "
        "When providing its analysis, Chart Ninja generates a concise signal that includes: "
        "- Action: Buy or Sell indication (NEVER GIVE HOLD ACTION BECAUSE TRADERS ARE LOOKING FOR POSITION!), "
        "- Optimal Entry Price: The precise price for initiating a position & why (GIVE EXACT PRICE), "
        "- Stop-Loss & Take-Profit Levels: Provide an unordered list of Stop-Loss & Take-Profit Levels corresponding to each of the different trading styles Day trading, Position trading, Momentum trading, Trend trading, News trading, Breakout trading, Retracement trading, Fundamental trading, Carry trade, Scalping, Swing trading, Long-term trading enabling users to tailor their strategies (INCLUDE WHY), "
        "- Disclaimer: This is not financial advice, Please do your own research, This disclaimer emphasizes the analytical nature of the tool without making guarantees, "
        "Additional information, if provided, is placed between the signal and the disclaimer, It is a succinct summary explaining the rationale behind the signal, "
        "Chart Ninja conducts thorough analysis and presents the signal first, followed by any additional insights, "
        "The tool is programmed to adapt its analysis to specific chart details without asking further questions from the user."
    )

    result = analyze_image_with_openai(image_path, api_key, long_prompt)
    print(result)
