import streamlit as st
import requests
import zipfile
import io

st.title("Téléchargement d'images Krys")

st.write("Cliquez sur le bouton ci-dessous pour télécharger l'ensemble des images dans un fichier ZIP.")

# Liste complète des URLs
urls = [
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/63a2e633f3acf_Header_krys.com_2022_12_21T115531.547.png",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/658aa0bb072f0_65859059160cc_03_v2.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/6639fe3190365_66279fb35459e_00055_DIGITAL_ELEMENTS_OP_KRYS_MAI_OO_LATCHPANEL_1690x950.png",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/67ab5e26003b2_KRYS_FRENCH_DISORDER_2480X1600_HEADER_PAGE_CATALOGUE_V2.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/658aa0c7a6206_65859059160cc_03_v2.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/5ec3febe9118c_5e67d0f673763_5da82e0b20df6_img_lentille_3x.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/5e67d0f673763_5da82e0b20df6_img_lentille_3x.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/5ec3fedb01fcc_5e67d0f673763_5da82e0b20df6_img_lentille_3x_1_.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/661e9464589a7_LV_1066S_WEB_32676_NO_LOGO_3800x2138.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/67b488a7a69b4_Header_Enfant_SK_solaire_2025_1_.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/662a5c2cf05af_Header_catalogue_page_OR0114_21G_SunWom_3800x2138px_NO_LOGO_1_.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/658aa0a59c9c0_6585935fb35bc_05_v2_Palmier_2.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/6606d953ba199_2402_BA_KrysGroupe_Header_L3800xH2138px2.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/674d94c4a3dbe_146878_622062L_BOSS_1718S_3800x2400px.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/665442b643e7d_Design_sans_titre_28_.png",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/658aa0a9774f1_6585935fb35bc_05_v2_Palmier_2.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/67b488fe49c5a_Header_Enfant_SK_solaire_2025_1_.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/665444b4e6699_2024_02_Header_KRYS_A_2_.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/658aa0c47f344_6585935fb35bc_05_v2_Palmier_2.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/66e2fe960c79c_66e19cc727934_RL7088_3800x2400PX_NOLOGO.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/6606e0043e9c8_MARC_747S_WEB_32104_NO_LOGO_3800x2137.5.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/67092110b2490_670538473a144_Final_HEADER_129035_24_MALA_MV_LACOSTE_KrysGroup_FW24visuals_Sun_Digital_CM.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/6690fdf0517c0_Copie_de_KRYS_LCS_5760x3840_HEADER_STORE_LOC_AD_DIGIT_05.png",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/618a88fc0d2ec_LSP_Homepage_16_9_2.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/661e90e890532_65d62a0c95827_LV_5052S_WEB_32680_NO_LOGO_3800x2138.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/658aa0d1dd14c_6585935fb35bc_05_v2_Palmier_2.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/665445a209ed0_Design_sans_titre_24_.png",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/6585793be1371_65799cbca3aa1_KRYS_3800x1500px.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/66e2f94d6fdc0_Header_Krys_2_.png",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/66e2f4081efa0_Header_Krys_1_.png",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/66e300683fcf2_Header_Krys_11_.png",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/6662cb9845237_Lenny_Kravitz_Ray_Ban_A_0363_R5_FOGRA39v2.png",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/658593e4dabdc_02_v2.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/670925b0e931c_6706526baddd6_Sandro_solaire_2024_3800x2140_px.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/67b5bc123db49_Header_Femme_SK_solaire_2025_1_.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/63d92cabc75d5_63ce9a9a16a76_Header_krys.com_2023_01_23T153218.818.png",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/65bcedd65537e_KRYS_GROUP_Header_16_9eme_3800x2155px_ski_1_1_.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/662a5e0d6d6ff_137101_580212L_TH_2088S_WEB_NO_LOGO_3800x1500.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/672a049f21c76_67223487d72e6_WOOW_KRYS_3800x2137px_OCT20243.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/649ea9fc7bd95_img8.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/65859059160cc_03_v2.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/65858f13a9cb9_07_v2.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/6606d854f1c1a_2402_BA_KrysGroupe_Header_L3800xH2138px.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/66f6a3991370e_66f40d1de3204_Header_Krys_12_1_.png",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/658afcaf3233e_65859059160cc_03_v2.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/65d876d3d34c9_2024_02_Header_KRYS_B_1_.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/658afcc19b00e_65859059160cc_03_v2.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/673cb75f973aa_Header_Page_Catalogue_Lunettes_de_vue_Prada_Femme.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/672a01984b6f9_67223487d72e6_WOOW_KRYS_3800x2137px_OCT2024.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/658afcb864652_65859059160cc_03_v2.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/66544cc2e7281_ATELIER_KRYS_3800X1270_SLIDER_HOME_DESKTOP_01.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/6690fe0310394_Copie_de_KRYS_LCS_5760x3840_HEADER_STORE_LOC_KV_01.png",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/661e8e2084b42_65d62a2f8aef5_LV_1072_WEB_32678_NO_LOGO_3800x2138.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/665445812d2d7_1.png",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/63dbdf9dda048_Header_3800x1500px.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/66e2ea6f2f9e6_Design_sans_titre_42_.png",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/65859217c571e_01_v1.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/670924ca23a4c_670652067a6bc_Header_Krys_21_.png",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/675b07003f261_675b05ea7e16a_KRYS_SIGNATURE_25_5760x3840_HEADER_STORE_LOC_03.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/66544bb2a5267_SIRALYA_KRYS_3800X1270_SLIDER_HOME_DESKTOP_02.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/662a5e8490c86_137101_580211L_TH_2093_WEB_NO_LOGO_3800x1500.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/672a05507bf66_WOOW_KRYS_3800x2137px_OCT20245_1_.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/64390bba2f999_HEADER_STORELOC.png",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/675b07ac02e76_675b05d9c551a_KRYS_SIGNATURE_25_5760x3840_HEADER_STORE_LOC_04.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/64887576e881e_646327ef1923e_krys_module_choix_monture_3800x1500_20230516.png",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/63ef87bac4001_Bleu_Femme.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/63ef880a77de4_Graphique_Femme.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/63ef6bef4f950_GettyImages_1242040955.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/63ef88286fc00_Gtraphique_Homme.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/63ef6ba1b7181_GettyImages_90719446.jpg",
    "https://krys-krys-storage.omn.proximis.com/Imagestorage/images/705/1600/63efa3d1c29b3_Translucide_Homme_Copie.jpg"
]

# Fonction pour télécharger les images et créer un ZIP en mémoire
def create_zip(urls):
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zipf:
        for url in urls:
            try:
                response = requests.get(url)
                response.raise_for_status()
                # Utilise le nom du fichier depuis l'URL
                filename = url.split("/")[-1]
                zipf.writestr(filename, response.content)
            except Exception as e:
                st.error(f"Erreur lors du téléchargement de {url} : {e}")
    zip_buffer.seek(0)
    return zip_buffer

if st.button("Lancer le téléchargement"):
    zip_file = create_zip(urls)
    st.download_button(
        label="Télécharger le fichier ZIP",
        data=zip_file,
        file_name="images.zip",
        mime="application/zip"
    )
