# import uncurl

# print(uncurl.parse("curl 'https://fred.stlouisfed.org/graph/api/series/metadata/' \ -H 'authority: fred.stlouisfed.org' \ -H 'accept: application/json' \ -H 'dnt: 1' \ -H 'x-requested-with: XMLHttpRequest' \ -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36' \ -H 'content-type: application/json;charset=UTF-8' \ -H 'origin: https://fred.stlouisfed.org' \ -H 'sec-fetch-site: same-origin' \ -H 'sec-fetch-mode: cors' \ -H 'sec-fetch-dest: empty' \ -H 'referer: https://fred.stlouisfed.org/series/AAA' \ -H 'accept-language: en-US,en;q=0.9' \ --data-binary $'{\"hostName\":\"fred.stlouisfed.org\",\"series\":[],\"chart\":{\"labels\":{\"title\":\"Moody\'s Seasoned Aaa Corporate Bond Yield\",\"subtitle\":\"Source: Moody’s\",\"left_axis\":\"Percent\",\"right_axis\":\"\",\"bottom_axis\":\"\",\"bubble-size_axis\":\"\",\"footer\":\"2020 fred.stlouisfed.org\"},\"cosd\":\"1919-01-01\",\"coed\":\"2020-04-01\",\"min_date\":\"1919-01-01\",\"max_date\":\"2020-04-01\",\"frequency\":\"Monthly\",\"width\":\"748\",\"height\":450,\"drp\":0,\"stacking\":null,\"txtcolor\":\"#444444\",\"mode\":\"fred\",\"ts\":\"12\",\"tts\":\"12\",\"fo\":\"open sans\",\"x_scale\":\"time\",\"trc\":0,\"nt\":0,\"thu\":0,\"bgcolor\":\"#e1e9f0\",\"graph_bgcolor\":\"#ffffff\",\"showLegend\":\"yes\",\"showAxisTitles\":\"yes\",\"zoomType\":\"x\",\"showTooltip\":\"yes\",\"chartType\":\"line\",\"recession_bars\":\"on\",\"showNavigator\":\"true\",\"available_chart_types\":[\"line\",\"area\",\"column\",\"scatter\",\"pie\",\"bubble\"],\"log_scales\":{\"left\":false,\"right\":false,\"bottom\":false,\"bubble-size\":false},\"available_stacking\":[\"normal\",\"percent\"],\"legacy_url\":\"bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1168&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=AAA&scale=left&cosd=1919-01-01&coed=2020-04-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Monthly&fam=avg&fgst=lin&fgsnd=2009-06-01&line_index=1&transformation=lin&vintage_date=2020-05-01&revision_date=2020-05-01&nd=1919-01-01\",\"piedate\":null,\"lastModified\":\"Fri, 01 May 2020 15:16:01 GMT\",\"obsFetch\":true,\"data_min\":-1609437600000,\"data_max\":1585717200000,\"data_num_obs\":1216},\"xAxis\":{},\"yAxis\":{},\"seriesObjects\":[{\"type\":\"time-series\",\"line_index\":1,\"legendIndex\":1,\"title\":\"Moody\'s Seasoned Aaa Corporate Bond Yield\",\"hide_marks\":true,\"available_formula_transformations\":{\"lin\":{\"full\":\"\",\"short\":\"\"},\"chg\":{\"full\":\"Change\",\"short\":\"Chg.\"},\"ch1\":{\"full\":\"Change from Year Ago\",\"short\":\"Chg. from Yr. Ago\"},\"pch\":{\"full\":\"Percent Change\",\"short\":\"% Chg.\"},\"pc1\":{\"full\":\"Percent Change from Year Ago\",\"short\":\"% Chg. from Yr. Ago\"},\"pca\":{\"full\":\"Compounded Annual Rate of Change\",\"short\":\"Comp. Annual Rate of Chg.\"},\"cch\":{\"full\":\"Continuously Compounded Rate of Change\",\"short\":\"Cont. Comp. Rate of Chg.\"},\"cca\":{\"full\":\"Continuously Compounded Annual Rate of Change\",\"short\":\"Cont. Comp. Annual Rate of Chg.\"},\"log\":{\"full\":\"Natural Log\",\"short\":\"Log\"},\"nbd\":{\"full\":\"Index (Scale value to 100 for chosen period)\",\"short\":\"Index\"}},\"line_color\":\"#4572a7\",\"line_style\":\"solid\",\"lw\":2,\"mark_type\":\"none\",\"mw\":3,\"scale\":\"left\",\"decimal_places\":\"2\",\"frequency\":\"Monthly\",\"fq\":\"Monthly\",\"available_colors\":{\"1\":\"#4572A7\",\"2\":\"#AA4643\",\"3\":\"#89A54E\",\"4\":\"#80699B\",\"5\":\"#3D96AE\",\"6\":\"#DB843D\",\"7\":\"#92A8CD\",\"8\":\"#A47D7C\",\"9\":\"#B5CA92\",\"10\":\"#91e8e1\",\"11\":\"#8d4653\",\"12\":\"#8085e8\"},\"available_fams\":{\"Average\":\"avg\",\"Sum\":\"sum\",\"End of Period\":\"eop\"},\"fam\":\"avg\",\"available_fqs\":[\"Monthly\",\"Quarterly\",\"Semiannual\",\"Annual\"],\"fml\":\"a\",\"fgst\":\"lin\",\"fgsnd\":\"2009-06-01\",\"all_fred_series_have_same_frequency\":true,\"has_fred_series_with_nbd_transformation\":false,\"cosd\":\"1919-01-01\",\"coed\":\"2020-04-01\",\"min_date\":\"1919-01-01\",\"max_date\":\"2020-04-01\",\"year_range\":101,\"ost\":-99999,\"oet\":99999,\"available_mmas\":[0,1,2],\"mma\":0,\"graph_series_ids\":[\"AAA\"],\"series_objects\":{\"a\":{\"series_id\":\"AAA\",\"title\":\"Moody\'s Seasoned Aaa Corporate Bond Yield\",\"season\":\"Not Seasonally Adjusted\",\"season_short\":\"NSA\",\"frequency\":\"Monthly\",\"frequency_short\":\"M\",\"units\":\"Percent\",\"units_short\":\"%\",\"keywords\":\"   \",\"notes\":\"These instruments are based on bonds with maturities 20 years and above. \\n\\n© 2017, Moody’s Corporation, Moody’s Investors Service, Inc., Moody’s Analytics, Inc. and/or their licensors and affiliates (collectively, “Moody’s”).  All rights reserved. Moody’s ratings and other information (“Moody’s Information”) are proprietary to Moody’s and/or its licensors and are protected by copyright and other intellectual property laws.  Moody’s Information is licensed to Client by Moody’s.  MOODY’S INFORMATION MAY NOT BE COPIED OR OTHERWISE REPRODUCED, REPACKAGED, FURTHER TRANSMITTED, TRANSFERRED, DISSEMINATED, REDISTRIBUTED OR RESOLD, OR STORED FOR SUBSEQUENT USE FOR ANY SUCH PURPOSE, IN WHOLE OR IN PART, IN ANY FORM OR MANNER OR BY ANY MEANS WHATSOEVER, BY ANY PERSON WITHOUT MOODY’S PRIOR WRITTEN CONSENT.\",\"all_obs_transformations\":{\"lin\":\"Percent\",\"cap\":\"Percent per Capita\",\"chg\":\"Change, Percent\",\"ch1\":\"Change from Year Ago, Percent\",\"pch\":\"Percent Change\",\"pc1\":\"Percent Change from Year Ago\",\"pca\":\"Compounded Annual Rate of Change\",\"cch\":\"Continuously Compounded Rate of Change\",\"cca\":\"Continuously Compounded Annual Rate of Change\"},\"abbreviated_all_obs_transformations\":{\"lin\":\"Levels\",\"cap\":\"Levels per Capita\",\"chg\":\"Chg.\",\"ch1\":\"Chg. from Yr. Ago\",\"pch\":\"% Chg.\",\"pc1\":\"% Chg. from Yr. Ago\",\"pca\":\"Comp. Annual Rate of Chg.\",\"cch\":\"Cont. Comp. Rate of Chg.\",\"cca\":\"Cont. Comp. Annual Rate of Chg.\",\"log\":\"Log\"},\"obs_transformations\":{\"lin\":\"Percent\",\"chg\":\"Change, Percent\",\"ch1\":\"Change from Year Ago, Percent\",\"pch\":\"Percent Change\",\"pc1\":\"Percent Change from Year Ago\",\"pca\":\"Compounded Annual Rate of Change\",\"cch\":\"Continuously Compounded Rate of Change\",\"cca\":\"Continuously Compounded Annual Rate of Change\"},\"valid_start_date\":\"2020-05-01\",\"valid_end_date\":\"2020-05-01\",\"vintage_date\":\"2020-05-01\",\"available_revision_dates\":[\"2020-05-01\"],\"revision_date\":\"2020-05-01\",\"relative_vintage\":null,\"nd\":\"1919-01-01\",\"step_line\":\"f\",\"transformation\":\"lin\",\"available_units\":{\"lin\":\"Percent\",\"chg\":\"Change, Percent\",\"ch1\":\"Change from Year Ago, Percent\",\"pch\":\"Percent Change\",\"pc1\":\"Percent Change from Year Ago\",\"pca\":\"Compounded Annual Rate of Change\",\"cch\":\"Continuously Compounded Rate of Change\",\"cca\":\"Continuously Compounded Annual Rate of Change\"},\"min_valid_start_date\":\"2020-05-01\",\"max_valid_start_date\":null,\"min_obs_start_date\":\"1919-01-01\",\"max_obs_start_date\":\"2020-04-01\",\"last_updated\":\"2020-05-01 10:16:01-05\"}},\"lsv\":null,\"lev\":null,\"observation_grouping_approximation\":\"close\",\"chart_key\":\"e0898c6381b800d217435ab94cdcbd25\"}],\"fredLogo\":{\"width\":105,\"height\":22,\"image\":\"https://fred.stlouisfed.org/images/fredgraph-logo-2x.png\"},\"container\":{\"width\":748,\"height\":450},\"defaultFontSize\":12,\"defaultMaxTicks\":10,\"showNavigator\":true,\"showCredits\":true,\"userNotices\":[],\"dataParams\":{},\"dataUrl\":\"https://fred-sa.stlouisfed.org/graph/graph-data.php\",\"graphBreakpointWidth\":400,\"observations\":{},\"axisTitleHeight\":300,\"titleWidth\":583,\"alignTicks\":true,\"borderRadius\":0,\"recessionBars\":\"on\",\"spacingBottom\":15,\"spacingTop\":50,\"spacingRight\":20,\"zoomType\":\"x\",\"style\":{\"fontFamily\":\"Open Sans\",\"color\":\"color: rgb(68, 68, 68)\"},\"chartTypes\":{\"line\":\"LINE\",\"area\":\"AREA\",\"column\":\"BAR\",\"scatter\":\"PLOT\",\"pie\":\"SEGMENT\"},\"chartTypeIcons\":{\"line\":\"fa-line-chart\",\"area\":\"fa-area-chart\",\"column\":\"fa-bar-chart\",\"pie\":\"fa-pie-chart\",\"scatter\":\"\"}}' \ --compressed"
# ))

from aiohttp import web
import json
import requests

async def handle(request):
    response_obj = { 'status' : 'success' }
    response_obj = use_external_api()
    # return response_obj.text
    return web.Response(text=json.dumps(json.loads(response_obj.text)))

def use_external_api():
    responses = requests.get('https://financialmodelingprep.com/api/v3/company/profile/AAPL')
    print(responses)
    return responses

async def new_user(request):
    try:
        # happy path where name is set
        user = request.query['name']
        # Process our new user
        print("Creating new user with name: " , user)

        response_obj = { 'status' : 'success' }
        response_obj = use_external_api()
        # return a success json response with status code 200 i.e. 'OK'
        return web.Response(text=json.dumps(response_obj), status=200)
    except Exception as e:
        # Bad path where name is not set
        response_obj = { 'status' : 'failed', 'reason': str(e) }
        # return failed with a status code of 500 i.e. 'Server Error'
        return web.Response(text=json.dumps(response_obj), status=500)

app = web.Application()
app.router.add_get('/', handle)
app.router.add_post('/user', new_user)

web.run_app(app)