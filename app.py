import sys
import types
import os

# 🚨 DYNAMIC FIX: Python 3.13 Compatibility Patches
if 'audioop' not in sys.modules:
    dummy_audioop = types.ModuleType('audioop')
    dummy_audioop.error = Exception
    sys.modules['audioop'] = dummy_audioop

import gradio as gr
from PIL import Image
import numpy as np

# Heuristic Simulation Mock Engine for Edge Hardware Verification
def analyze_crop_health(input_image, total_field_area, chemical_type):
    if input_image is None:
        return "⚠️ Error: Please upload or capture a crop image first!", None
        
    # Process image matrix properties natively
    img = Image.fromarray(input_image.astype('uint8'), 'RGB')
    img_np = np.array(img)
    
    # Simulating localized pixel intensity tracking for crop vs weed detection
    green_intensity = np.mean(img_np[:, :, 1]) 
    weed_density_percentage = min(95.0, max(5.0, (green_intensity / 255.0) * 100.0 - 10.0))
    
    # Dosage Calculation Core Matrix Logic
    base_rates = {
        "Broadleaf Selective (e.g., 2,4-D)": 0.5,
        "Grassy Weed Killer (e.g., Quizalofop)": 0.4,
        "Non-Selective Knockdown (e.g., Glyphosate)": 1.0
    }
    
    rate_per_acre = base_rates.get(chemical_type, 0.5)
    
    # Calculations based on the weed infestation density
    targeted_area_acres = total_field_area * (weed_density_percentage / 100.0)
    required_chemical_liters = targeted_area_acres * rate_per_acre
    required_water_liters = required_chemical_liters * 200 # Standard 1:200 dilution rule
    
    # Savings calculation compared to blank spray coverage
    blank_spray_chemical = total_field_area * rate_per_acre
    chemical_saved = max(0.0, blank_spray_chemical - required_chemical_liters)
    money_saved_pkr = chemical_saved * 2500 # Avg cost constant per liter in PKR
    
    # 🌐 Bilingual Analysis Report Output Formatting (Strict Inline Color Injection)
    report_markdown = f"""
    <div style='color: #0f172a !important;'>
    
    ### <span style='color: #1e293b !important;'>📊 Real-Time Diagnostic Report // تشخیص کی رپورٹ</span>
    <p style='color: #475569 !important; margin: 0;'>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</p>
    
    * <span style='color: #334155 !important;'>**Weed Infestation Density (جڑی بوٹیوں کی کثافت):**</span> <span style='background-color: #f1f5f9; color: #0f172a; padding: 2px 6px; border-radius: 4px; font-weight: bold;'>{weed_density_percentage:.2f}%</span>
    * <span style='color: #334155 !important;'>**Targeted Spray Area (مطلوبہ سپرے کا رقبہ):**</span> <span style='background-color: #f1f5f9; color: #0f172a; padding: 2px 6px; border-radius: 4px; font-weight: bold;'>{targeted_area_acres:.3f} Acres</span> (out of {total_field_area} acres)
    
    ### <span style='color: #1e293b !important;'>🧪 Precise Herbicide Recipe // سپرے کا درست تناسب</span>
    <p style='color: #475569 !important; margin: 0;'>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</p>
    
    * <span style='color: #334155 !important;'>**Required Weedicide (ضروری زہر):**</span> 🟢 <span style='background-color: #16a34a; color: #ffffff; padding: 2px 8px; border-radius: 4px; font-weight: bold;'>{required_chemical_liters:.3f} Liters</span>
    * <span style='color: #334155 !important;'>**Water Dilution Mix (پانی کی مقدار):**</span> 💧 <span style='background-color: #2563eb; color: #ffffff; padding: 2px 8px; border-radius: 4px; font-weight: bold;'>{required_water_liters:.1f} Liters</span> (Tank Mix)
    * <span style='color: #334155 !important;'>**Recommended Pressure Node:**</span> <span style='background-color: #334155; color: #ffffff; padding: 2px 6px; border-radius: 4px; font-size: 13px;'>Low-Drift Flat Fan Nozzle (2-3 Bar)</span>
    
    ### <span style='color: #1e293b !important;'>💰 Eco-Savings & Financial Impact // بچت کا تخمینہ</span>
    <p style='color: #475569 !important; margin: 0;'>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</p>
    
    * <span style='color: #334155 !important;'>**Chemical Quantity Saved (زہر کی بچت):**</span> <span style='background-color: #f1f5f9; color: #0f172a; padding: 2px 6px; border-radius: 4px; font-weight: bold;'>{chemical_saved:.3f} Liters</span>
    * <span style='color: #334155 !important;'>**Direct Cost Reduction (پیسوں کی بچت):**</span> 🎉 <span style='background-color: #eab308; color: #0f172a; padding: 2px 8px; border-radius: 4px; font-weight: bold;'>Rs. {money_saved_pkr:,.0f} PKR</span>
    
    <p style='margin-top: 15px; font-size: 13px; color: #16a34a; font-style: italic; font-weight: 500;'>💡 Advantage: Shifting from blanket spray to targeted spot application prevents soil toxicity and protects local groundwater tables.</p>
    
    </div>
    """
    
    # Generate visual feedback (simulating edge bounding mask overlays)
    mask_img = img_np.copy()
    mask_img[:, :, 0] = np.where(mask_img[:, :, 1] > 100, mask_img[:, :, 0] + 50, mask_img[:, :, 0])
    output_preview = Image.fromarray(np.clip(mask_img, 0, 255).astype('uint8'), 'RGB')
    
    return report_markdown, output_preview

# 🔥 FORCE DISCIPLINE: Direct Global HTML & Component Font Overrides
custom_css = """
body, .gradio-container { background-color: #f8fafc !important; color: #0f172a !important; font-family: 'Segoe UI', system-ui, sans-serif; }
.farm-btn { background-color: #16a34a !important; color: #ffffff !important; font-weight: bold !important; border-radius: 8px !important; font-size: 16px !important; border: none !important; margin-top: 10px; }
.farm-btn:hover { background-color: #15803d !important; box-shadow: 0 4px 12px rgba(22,163,74,0.2); }
.green-panel { border: 1px solid #e2e8f0 !important; border-radius: 12px; padding: 20px; background: #ffffff !important; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }
input, select, textarea { background-color: #ffffff !important; color: #0f172a !important; border: 1px solid #cbd5e1 !important; }
label { color: #334155 !important; font-weight: 600 !important; }

/* Global overrides targeting inner markdown wrappers specifically */
.prose, .prose * { color: #0f172a !important; }
.markdown-text * { color: #0f172a !important; }
"""

with gr.Blocks(title="Smart Crop Weed Spotter v1.0", css=custom_css, theme=gr.themes.Default(primary_hue="green", secondary_hue="slate")) as demo:
    gr.HTML(
        """
        <div style="text-align: center; margin-bottom: 25px; padding: 20px; background: #16a34a; border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);">
            <h1 style='margin: 0; font-size: 28px; color: #ffffff; letter-spacing: 0.5px; font-weight: 700;'>🌱 SMART CROP WEED SPOTTER & CALCULATOR</h1>
            <p style='margin: 6px 0 0 0; color: #f0fdf4; font-size: 14px; font-weight: 500;'>Offline Edge Vision Simulation // Ultra-Lightweight Precise Farm Logistics</p>
        </div>
        """
    )
    
    with gr.Row():
        with gr.Column(scale=4, elem_classes="green-panel"):
            gr.Markdown("### 📸 Field Scanner Input Node")
            input_img = gr.Image(label="Upload Crop Image or Snap Photo", sources=["upload", "webcam"], type="numpy")
            
            with gr.Row():
                field_size = gr.Number(label="Total Field Size (Acres)", value=1.0, minimum=0.1)
                chem_type = gr.Dropdown(
                    label="Select Herbicide Type", 
                    choices=["Broadleaf Selective (e.g., 2,4-D)", "Grassy Weed Killer (e.g., Quizalofop)", "Non-Selective Knockdown (e.g., Glyphosate)"],
                    value="Broadleaf Selective (e.g., 2,4-D)"
                )
                
            scan_btn = gr.Button("🎯 Run Edge Scan & Calculate Dosage", elem_classes="farm-btn")
            
        with gr.Column(scale=5, elem_classes="green-panel"):
            gr.Markdown("### ⚡ Edge Computer Output Analysis")
            
            # Added dynamic elem_id to ensure strict styling enforcement
            results_manifest = gr.Markdown("`System standing by. Please inject crop visual diagnostics metadata...`", elem_id="diagnostic-output")
            output_mask = gr.Image(label="Edge Detection Highlight Mapping (Weed Regions)")

    scan_btn.click(
        fn=analyze_crop_health, 
        inputs=[input_img, field_size, chem_type], 
        outputs=[results_manifest, output_mask]
    )

demo.launch()
