### Pillow, PIL로 가능한 기능들

<ol>
    <li> 픽셀 단위 조작
    <li> 마스킹 및 투명도 제어
    <li> 흐림, 윤곽 보정 다듬어 윤곽 검출 등의 이미지 필터
    <li> 선명하게, 밝기 보정, 명암 보정, 색 보정 등의 화상 조정
    <li> 이미지에 텍스트 추가 기타 등등
</ol>

<p>
    RGB
    <ul>
    <li>1 (1비트 픽셀, 흑백, 바이트당 1픽셀로 저장)
    <li>L (8비트 픽셀, 흑백)
    <li>P (8비트 픽셀, 색상 팔레트를 사용하여 다른 모드에 매핑됨)
    <li>RGB (3x8비트 픽셀, 트루 컬러)
    <li>RGBA (4x8비트 픽셀, 투명 마스크가 있는 트루 컬러)
    <li>CMYK (4x8비트 픽셀, 색상 분리)
    <li>YCbCr (3x8비트 픽셀, 컬러 비디오 형식)
    <li>LAB (3x8비트 픽셀, Lab 색 공간)
    <li>HSV (3x8비트 픽셀, 색조, 채도, 값 색 공간)
    <li>I (32비트 부호 있는 정수 픽셀)
    <li>F (32비트 부동 소수점 픽셀)
    </ul>
</p>

<p>
    ImageFilter
    <ul>
        <li> BLUR : BLUR, BoxBlur( ), GaussianBlur( )
        <li> MedianFilter( ), MinFilter( ), MaxFilter( ) 등
        <li> CONTOUR
        <li> DETAIL
        <li> EDGE_ENHANCE, EDGE_ENHANCE_MORE
        <li> EMBOSS
        <li> FIND_EDGES
        <li> SHARPEN
        <li> SMOOTH, SMOOTH_MORE
    </ul>
</p>