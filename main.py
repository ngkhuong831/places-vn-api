from fastapi import FastAPI

app = FastAPI()

@app.get('/')

async def root():
    return [
 {
  "id": "01",
  "name": "Thành phố Hà Nội",
  "lat": 21.028333,
  "lon": 105.853333
 },
 {
  "id": "02",
  "name": "Tỉnh Hà Giang",
  "lat": 22.8168,
  "lon": 104.980738
 },
 {
  "id": "04",
  "name": "Tỉnh Cao Bằng",
  "lat": 22.685618,
  "lon": 106.263084
 },
 {
  "id": "06",
  "name": "Tỉnh Bắc Kạn",
  "lat": 22.161335,
  "lon": 105.830498
 },
 {
  "id": "08",
  "name": "Tỉnh Tuyên Quang",
  "lat": 21.777355,
  "lon": 105.228424
 },
 {
  "id": "10",
  "name": "Tỉnh Lào Cai",
  "lat": 22.379997,
  "lon": 104.15786
 },
 {
  "id": "11",
  "name": "Tỉnh Điện Biên",
  "lat": 21.385396,
  "lon": 103.013913
 },
 {
  "id": "12",
  "name": "Tỉnh Lai Châu",
  "lat": 22.362776,
  "lon": 103.265991
 },
 {
  "id": "14",
  "name": "Tỉnh Sơn La",
  "lat": 21.328716,
  "lon": 103.914528
 },
 {
  "id": "15",
  "name": "Tỉnh Yên Bái",
  "lat": 21.693161,
  "lon": 104.872742
 },
 {
  "id": "17",
  "name": "Tỉnh Hoà Bình",
  "lat": 20.725,
  "lon": 105.2333
 },
 {
  "id": "19",
  "name": "Tỉnh Thái Nguyên",
  "lat": 21.564225,
  "lon": 105.879364
 },
 {
  "id": "20",
  "name": "Tỉnh Lạng Sơn",
  "lat": 21.853851,
  "lon": 106.761189
 },
 {
  "id": "22",
  "name": "Tỉnh Quảng Ninh",
  "lat": 21.250982,
  "lon": 107.193604
 },
 {
  "id": "24",
  "name": "Tỉnh Bắc Giang",
  "lat": 21.274838,
  "lon": 106.201583
 },
 {
  "id": "25",
  "name": "Tỉnh Phú Thọ",
  "lat": 21.262501,
  "lon": 105.125427
 },
 {
  "id": "26",
  "name": "Tỉnh Vĩnh Phúc",
  "lat": 21.363571,
  "lon": 105.548401
 },
 {
  "id": "27",
  "name": "Tỉnh Bắc Ninh",
  "lat": 21.187548,
  "lon": 106.073406
 },
 {
  "id": "30",
  "name": "Tỉnh Hải Dương",
  "lat": 20.93333,
  "lon": 106.31667
 },
 {
  "id": "31",
  "name": "Thành phố Hải Phòng",
  "lat": 20.866389,
  "lon": 106.6825
 },
 {
  "id": "33",
  "name": "Tỉnh Hưng Yên",
  "lat": 20.85432,
  "lon": 106.016006
 },
 {
  "id": "34",
  "name": "Tỉnh Thái Bình",
  "lat": 20.538935,
  "lon": 106.394348
 },
 {
  "id": "35",
  "name": "Tỉnh Hà Nam",
  "lat": 20.585867,
  "lon": 105.923996
 },
 {
  "id": "36",
  "name": "Tỉnh Nam Định",
  "lat": 20.25,
  "lon": 106.25
 },
 {
  "id": "37",
  "name": "Tỉnh Ninh Bình",
  "lat": 20.250924,
  "lon": 105.974808
 },
 {
  "id": "38",
  "name": "Tỉnh Thanh Hóa",
  "lat": 19.8075,
  "lon": 105.776389
 },
 {
  "id": "40",
  "name": "Tỉnh Nghệ An",
  "lat": 19.176301,
  "lon": 104.977112
 },
 {
  "id": "42",
  "name": "Tỉnh Hà Tĩnh",
  "lat": 18.341002,
  "lon": 105.907345
 },
 {
  "id": "44",
  "name": "Tỉnh Quảng Bình",
  "lat": 17.468573,
  "lon": 106.254272
 },
 {
  "id": "45",
  "name": "Tỉnh Quảng Trị",
  "lat": 16.830832,
  "lon": 107.067261
 },
 {
  "id": "46",
  "name": "Tỉnh Thừa Thiên Huế",
  "lat": 16.463744,
  "lon": 107.58482
 },
 {
  "id": "48",
  "name": "Thành phố Đà Nẵng",
  "lat": 16.076667,
  "lon": 108.222778
 },
 {
  "id": "49",
  "name": "Tỉnh Quảng Nam",
  "lat": 15.556898,
  "lon": 108.0368
 },
 {
  "id": "51",
  "name": "Tỉnh Quảng Ngãi",
  "lat": 15.123875,
  "lon": 108.811727
 },
 {
  "id": "52",
  "name": "Tỉnh Bình Định",
  "lat": 14.195163,
  "lon": 108.880005
 },
 {
  "id": "54",
  "name": "Tỉnh Phú Yên",
  "lat": 13.090179,
  "lon": 109.091492
 },
 {
  "id": "56",
  "name": "Tỉnh Khánh Hòa",
  "lat": 12.073058,
  "lon": 109.047768
 },
 {
  "id": "58",
  "name": "Tỉnh Ninh Thuận",
  "lat": 11.565556,
  "lon": 108.990278
 },
 {
  "id": "60",
  "name": "Tỉnh Bình Thuận",
  "lat": 11.100252,
  "lon": 108.141174
 },
 {
  "id": "62",
  "name": "Tỉnh Kon Tum",
  "lat": 14.351543,
  "lon": 108.000412
 },
 {
  "id": "64",
  "name": "Tỉnh Gia Lai",
  "lat": 13.904742,
  "lon": 108.179626
 },
 {
  "id": "66",
  "name": "Tỉnh Đắk Lắk",
  "lat": 12.766268,
  "lon": 108.325195
 },
 {
  "id": "67",
  "name": "Tỉnh Đắk Nông",
  "lat": 12.256812,
  "lon": 107.701721
 },
 {
  "id": "68",
  "name": "Tỉnh Lâm Đồng",
  "lat": 11.684514,
  "lon": 108.141174
 },
 {
  "id": "70",
  "name": "Tỉnh Bình Phước",
  "lat": 11.755781,
  "lon": 106.719818
 },
 {
  "id": "72",
  "name": "Tỉnh Tây Ninh",
  "lat": 11.367795,
  "lon": 106.119003
 },
 {
  "id": "74",
  "name": "Tỉnh Bình Dương",
  "lat": 11.162235,
  "lon": 106.625061
 },
 {
  "id": "75",
  "name": "Tỉnh Đồng Nai",
  "lat": 11.05443,
  "lon": 107.146912
 },
 {
  "id": "77",
  "name": "Tỉnh Bà Rịa - Vũng Tàu",
  "lat": 10.410157,
  "lon": 107.136555
 },
 {
  "id": "79",
  "name": "Thành phố Hồ Chí Minh",
  "lat": 10.769444,
  "lon": 106.681944
 },
 {
  "id": "80",
  "name": "Tỉnh Long An",
  "lat": 10.691647,
  "lon": 106.204834
 },
 {
  "id": "82",
  "name": "Tỉnh Tiền Giang",
  "lat": 10.420288,
  "lon": 106.296844
 },
 {
  "id": "83",
  "name": "Tỉnh Bến Tre",
  "lat": 10.248371,
  "lon": 106.376152
 },
 {
  "id": "84",
  "name": "Tỉnh Trà Vinh",
  "lat": 9.813946,
  "lon": 106.298904
 },
 {
  "id": "86",
  "name": "Tỉnh Vĩnh Long",
  "lat": 10.244823,
  "lon": 105.959015
 },
 {
  "id": "87",
  "name": "Tỉnh Đồng Tháp",
  "lat": 10.575572,
  "lon": 105.682983
 },
 {
  "id": "89",
  "name": "Tỉnh An Giang",
  "lat": 10.381116,
  "lon": 105.419884
 },
 {
  "id": "91",
  "name": "Tỉnh Kiên Giang",
  "lat": 9.836273,
  "lon": 105.125427
 },
 {
  "id": "92",
  "name": "Thành phố Cần Thơ",
  "lat": 10.032415,
  "lon": 105.784092
 },
 {
  "id": "93",
  "name": "Tỉnh Hậu Giang",
  "lat": 9.764551,
  "lon": 105.640411
 },
 {
  "id": "94",
  "name": "Tỉnh Sóc Trăng",
  "lat": 9.6,
  "lon": 105.9
 },
 {
  "id": "95",
  "name": "Tỉnh Bạc Liêu",
  "lat": 9.312214,
  "lon": 105.493469
 },
 {
  "id": "96",
  "name": "Tỉnh Cà Mau",
  "lat": 9.061414,
  "lon": 105.032043
 }
]